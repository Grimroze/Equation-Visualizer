import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def threedim():
    eq_list = [i.strip().lower() for i in equation_input.split(",")]

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(12, 6))

    for i, eq in enumerate(eq_list):
        try:
            Z = ne.evaluate(eq, local_dict={'x': X, 'y': Y, 'sin': np.sin, 'cos': np.cos, 'exp': np.exp})
            ax = fig.add_subplot(1, len(eq_list), i + 1, projection='3d')
            ax.plot_surface(X, Y, Z, cmap='plasma')
            ax.set_title(f"z = {eq}")
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")
        except Exception as e:
            print(f"Could not evaluate, Error'{eq}': {e}")

    plt.tight_layout()
    plt.show()


def twodim():
    equations = [eq.strip().lower() for eq in equation_input.split(",")]

    x = np.linspace(-10, 10, 500)

    plt.figure(figsize=(10, 6))

    # Plot each equation
    for eq in equations:
        try:
            y = ne.evaluate(eq,local_dict={'x': x, 'sin': np.sin, 'cos': np.cos, 'exp': np.exp} )
            plt.plot(x, y,label=f"y = {eq}")
        except Exception as e:
            print(f"Error evaluating '{eq}':", e)

    plt.title("Multiple 2D Equation Plotter")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

while True:

    num = int(input("Enter the number of dimensions (2,3): "))
    equation_input = input("Enter the number of equations(seperated by commas): ")

    if num == 3:
        threedim()
    elif num == 2:
        twodim()
    else:
        print("Invalid Dimensions")

    cont = input("Continue? (y/n): ").strip().lower()
    if cont != 'y':
        print("Exiting program...")
        break






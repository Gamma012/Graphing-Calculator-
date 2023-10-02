import matplotlib.pyplot as plt
import numpy as np

mode = str(input('Enter mode (graph or arithmetic): '))
if mode == 'arithmetic':
    n1 = float(input('enter first number: '))
    operation = str(input('enter operation (+, -, *, /): '))
    n2 = float(input('enter second number: '))

    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('ERROR: Invalid Operator')
    elif operation == '+':
        print('ans: ' + str(n1 + n2))
    elif operation == '-':
        print('ans: ' + str(n1 - n2))
    elif operation == '*':
        print('ans: ' + str(n1 * n2))
    elif operation == '/':
        print('ans: ' + str(n1 / n2))
        print('rounded ans: ' + str(n1 // n2))
        print('remainder: ' + str(n1 % n2))
elif mode == 'graph':
    x_start_point = float(input('Enter x axis lowest point: '))
    x_end_point = float(input('Enter x axis highest point: '))
    x = np.arange(x_start_point, x_end_point, 0.00001)
    graph_type = str(input('Enter graph type (linear, polynomial, exponential, circle): '))

    y = None

    if graph_type == 'linear':
        print('Enter values for m and c (y=mx+c): ')
        m = float(input('m = '))
        c = float(input('c = '))
        y = m * x + c
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        x_value = float(input('Enter x value'))
        y_value = m * x_value + c
    elif graph_type == 'polynomial':
        polynomial_type = str(input('Enter polynomial type (quadratic, cubic, quartic, quintic): '))
        if polynomial_type == 'quadratic':
            print('Enter coefficients for ax^2+bx+c: ')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
            y = a * x ** 2 + b * x + c
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()
            x_value = float(input('Enter x value'))
            y_value = a * x_value ** 2 + b * x + c
        elif polynomial_type == 'cubic':
            print('Enter coefficients for ax^3+bx^2+cx+d: ')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
            d = float(input('d = '))
            y = a * x ** 3 + b * x ** 2 + c * x + d
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()
            x_value = float(input('Enter x value'))
            y_value = a * x_value ** 3 + b * x_value ** 2 + c * x_value + d
        elif polynomial_type == 'quartic':
            print('Enter coefficients for ax^4+bx^3+cx^2+dx+e: ')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
            d = float(input('d = '))
            e = float(input('e = '))
            y = a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()
            x_value = float(input('Enter x value'))
            y_value = a * x_value ** 4 + b * x_value ** 3 + c * x_value ** 2 + d * x_value + e
        elif polynomial_type == 'quintic':
            print('Enter coefficients for ax^5+bx^4+cx^3+dx^2+ex+f: ')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
            d = float(input('d = '))
            e = float(input('e = '))
            f = float(input('f = '))
            y = a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.show()
            x_value = float(input('Enter x value'))
            y_value = a * x_value ** 5 + b * x_value ** 4 + c * x_value ** 3 + d * x_value ** 2 + e * x_value + f
        else:
            print('ERROR: Invalid Input')
    elif graph_type == 'exponential':
        print('Enter values for a, b and c (y=ab^cx+d)')
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        d = float(input('d = '))
        y = (a * (b ** (x * c))) + d
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        x_value = float(input('Enter x value'))
        y_value = (a * (b ** (x_value * c))) + d
    elif graph_type == 'circle':
        r = int(input('Enter radius of circle: '))
        cx = int(input('Enter x coordinate of center of circle: '))
        cy = int(input('Enter y coordinate of center of circle: '))
        y1 = cy + np.sqrt(np.power(r, 2) - np.power((x - cx), 2))
        plt.plot(x, y1, 'b')
        y2 = cy - np.sqrt(np.power(r, 2) - np.power((x - cx), 2))
        plt.plot(x, y2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    else:
        print('ERROR: Invalid Input')
else:
    print('ERROR: Invalid Input')

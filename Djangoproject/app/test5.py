class SimpleCalculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

def main():
    print("Welcome to the Simple Calculator!")
    
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    calculator = SimpleCalculator()
    
    # Perform calculations
    sum_result = calculator.add(num1, num2)
    product_result = calculator.multiply(num1, num2)

    # Display results
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The product of {num1} and {num2} is: {product_result}")

if __name__ == "__main__":
    main()









import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Example usage:
num1 = 12
num2 = 18
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")
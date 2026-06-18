a = 10
b = 20
if a != b:
    print("Values are different")
elif a == b:
    print("Values are equal")
else:
    pass
print(f"a={a}, b={b} -> Different check result in one line context above.")

# One-line expression demonstration below using the same variables:
result = 'Different' if a != b else 'Equal'
print(result)  # Output: Different

if __name__ == '__main__':
    pass

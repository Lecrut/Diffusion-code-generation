x = 10
y = 5
print("Condition met" if x > y else "Condition failed")
if __name__ == '__main__':
    print(f"{x} is {'greater than' if x > y else 'not greater than'} {y}")
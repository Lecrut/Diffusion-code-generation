def compare_numbers(a, b):
    try:
        int_a = int(a)
        int_b = int(b)
        if int_a > int_b:
            return 'Greater'
        elif int_b > int_a:
            return 'Lesser'
        else:
            return 'Equal'
    except ValueError:
        raise ValueError("Both inputs must be valid integers.")

if __name__ == '__main__':
    num1 = 42
    num2 = 7
    result = compare_numbers(num1, num2)
    print(result)
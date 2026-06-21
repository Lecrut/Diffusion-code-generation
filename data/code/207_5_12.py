def find_max_stringified_numbers(stringified_numbers):
    try:
        numbers = [int(num) for num in stringified_numbers if num.replace('.', '', 1).isdigit()]
        return max(numbers)
    except ValueError:
        raise ValueError("List contains non-numeric values")

if __name__ == '__main__':
    data1 = ["20", "30.5", "10", "-5"]
    print("Max of data1:", find_max_stringified_numbers(data1))
    
    data2 = ["-10", "-20", "-30", "-15"]
    print("Max of data2:", find_max_stringified_numbers(data2))

    data3 = ["abc", "123.4", "567"]
    try:
        print("Max of data3:", find_max_stringified_numbers(data3))
    except ValueError as e:
        print(e)
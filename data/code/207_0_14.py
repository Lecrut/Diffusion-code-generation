def find_max_element(numbers):
    return max(numbers)

if __name__ == '__main__':
    data = [12, 45, 7, 89, 3]
    max_value = find_max_element(data)
    print(f"The maximum value in {data} is: {max_value}")
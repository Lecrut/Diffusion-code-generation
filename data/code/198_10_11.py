if __name__ == '__main__':
    input_data = [42, 15, 89, 3, 77, 21]

    def find_min(numbers):
        if not numbers:
            raise ValueError("List is empty")
        return min(numbers)

    try:
        smallest = find_min(input_data)
        print(smallest)
    except ValueError as e:
        print(e)
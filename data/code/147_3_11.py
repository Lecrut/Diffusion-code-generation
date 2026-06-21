if __name__ == '__main__':
    numbers = [3.5, 1.2, 4.8, 2.9]
    try:
        if all(isinstance(x, float) for x in numbers):
            sorted_numbers = sorted(numbers, reverse=True)
            print(sorted_numbers)
        else:
            raise ValueError("All elements must be floats")
    except Exception as e:
        print(f"Error: {e}")
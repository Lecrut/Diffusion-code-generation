numbers = [3.5, 1.2, 4.8, 2.9]
sorted_numbers = sorted(numbers, reverse=True)
if __name__ == '__main__':
    try:
        if all(isinstance(x, float) for x in numbers):
            print(sorted_numbers)
        else:
            raise ValueError("All elements must be floats")
    except Exception as e:
        print(f"Error: {e}")
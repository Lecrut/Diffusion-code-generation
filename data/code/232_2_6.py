import itertools

def print_sequence():
    try:
        count = 20
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Count must be a positive integer")

        for number in itertools.count(1):
            if number > count:
                break
            print(number)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print_sequence()
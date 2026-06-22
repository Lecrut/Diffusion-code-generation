import itertools

def print_sequence():
    try:
        for number in itertools.count(1):
            if number > 20:
                break
            print(number)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print_sequence()
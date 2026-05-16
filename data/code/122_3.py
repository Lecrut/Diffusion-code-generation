import sys
def calculate_average(*args):
    if not args:
        return 0.0
    return sum(args) / len(args)
if __name__ == '__main__':
    test_args = [10.5, 20.5, 30.0, 40.0]
    average = calculate_average(*test_args)
    print(average)
import sys
def sum_three(*args):
    if len(args) != 3:
        raise ValueError("Exactly three numeric arguments are required.")
    return sum(args)
if __name__ == '__main__':
    result = sum_three(10, 20.5, 30)
    print(result)
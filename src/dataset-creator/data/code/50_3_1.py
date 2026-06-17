import sys
def sum_three(*args):
    if len(args) != 3:
        raise ValueError("Exactly three numeric arguments are required.")
    return args[0] + args[1] + args[2]
if __name__ == '__main__':
    result = sum_three(1, 2, 3)
    print(result)
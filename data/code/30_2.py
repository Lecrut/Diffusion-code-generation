import sys
if __name__ == '__main__':
    input_string = "abcdefgh"
    n = len(input_string)
    result = list(input_string)
    for i in range(0, n - 1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    print("".join(result))
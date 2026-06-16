import sys
def reverse_array(arr):
    return arr[::-1]
if __name__ == '__main__':
    data = [3, 6, 9, 24, 50, -7]
    result = reverse_array(data)
    print(result)
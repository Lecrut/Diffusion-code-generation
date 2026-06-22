MAX_NUM = 1000

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def order_three(a, b, c):
    numbers = [a, b, c]
    bubble_sort(numbers)
    return tuple(numbers)

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    num3 = 1
    result = order_three(num1, num2, num3)
    print(result)
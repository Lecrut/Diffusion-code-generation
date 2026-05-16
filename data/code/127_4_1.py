import sys
if __name__ == '__main__':
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for num in input_data:
        try:
            if isinstance(num, int):
                if num % 2 == 0:
                    print("Even")
                else:
                    print("Odd")
            else:
                print("Error: Non-integer input encountered")
        except TypeError:
            print("Error: Input type issue encountered")
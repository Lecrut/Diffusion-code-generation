def find_maximum(strings):
    if not strings:
        raise ValueError("Input list cannot be empty")
    return max(strings)

if __name__ == '__main__':
    data1 = ["apple", "banana", "cherry"]
    data2 = ["zebra", "yak", "xray", "whale"]
    data3 = ["single"]
    data4 = []
    print(f"Maximum of {data1}: {find_maximum(data1)}")
    print(f"Maximum of {data2}: {find_maximum(data2)}")
    print(f"Maximum of {data3}: {find_maximum(data3)}")
    try:
        print(f"Maximum of {data4}: {find_maximum(data4)}")
    except ValueError as e:
        print(f"Error: {e}")
def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10, 34, -5, 21, 67]
    try:
        print(f"Maximum of {sample_list}: {find_maximum(sample_list)}")
    except ValueError as e:
        print(e)
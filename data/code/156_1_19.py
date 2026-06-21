def validate_data(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def calculate_average(data):
    validate_data(data)
    return sum(data) / len(data)

if __name__ == '__main__':
    list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    
    try:
        avg1 = calculate_average(list1)
        print(f"Average of {list1}: {avg1}")
        avg2 = calculate_average(list2)
        print(f"Average of {list2}: {avg2}")
        calculate_average(empty_list)
    except ValueError as e:
        print(f"Error: {e}")
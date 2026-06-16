try:
    value1 = 5
    value2 = "5"
    result = value1 == value2
except TypeError as e:
    print(f"Error comparing types: {e}")
else:
    if result:
        print("Values are equal")
    else:
        print("Values are not equal")
if __name__ == '__main__':
    try:
        value1 = 5.0
        value2 = [5]
        comparison_result = value1 == value2
        if isinstance(comparison_result, bool):
            print(f"Comparison result (bool): {comparison_result}")
        else:
            print("Values are not comparable")
    except TypeError as e:
        print(f"Type error occurred: {e}")
def miles_to_centimeters(miles):
    try:
        return miles * 160934
    except TypeError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    result = miles_to_centimeters(5)
    print(result)
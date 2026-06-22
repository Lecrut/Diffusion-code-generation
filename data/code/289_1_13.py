def miles_to_centimeters(miles):
    try:
        return miles * 160934
    except TypeError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    sample_miles = 5
    result = miles_to_centimeters(sample_miles)
    print(result)
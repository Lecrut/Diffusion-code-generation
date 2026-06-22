def compare_length(miles: float, kilometers: float) -> str:
    miles_to_km = miles * 1.60934
    if miles_to_km > kilometers:
        return "Miles are greater"
    elif miles_to_km < kilometers:
        return "Kilometers are greater"
    else:
        return "Both are equal"

if __name__ == '__main__':
    result = compare_length(10, 16.0934)
    print(result)
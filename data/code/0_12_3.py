def convert_centimeters_to_inches(centimeters: float) -> float:
    return centimeters * 0.393701

if __name__ == '__main__':
    result = convert_centimeters_to_inches(50)
    print(result)
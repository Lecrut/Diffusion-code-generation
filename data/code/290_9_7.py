def validate_pounds(pounds):
    if not isinstance(pounds, (int, float)) or pounds < 0:
        raise ValueError("Pounds must be a non-negative number")

def pounds_to_ounces(pounds):
    validate_pounds(pounds)
    return int(pounds * 16)

if __name__ == '__main__':
    print(pounds_to_ounces(5))
    print(pounds_to_ounces(10))
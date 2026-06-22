def validate_mm(mm):
    if not isinstance(mm, (int, float)) or mm < 0:
        raise ValueError("Invalid millimeters value")

def mm_to_inches(mm):
    validate_mm(mm)
    return mm * 0.0393701

if __name__ == '__main__':
    print(mm_to_inches(25))
    print(mm_to_inches(100))
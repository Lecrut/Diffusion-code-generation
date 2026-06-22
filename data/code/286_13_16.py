CONVERSION_FACTOR = 0.0393701

def mm_to_inches(mm):
    return mm * CONVERSION_FACTOR

if __name__ == '__main__':
    print(f"25mm is equal to {mm_to_inches(25):.4f} inches")
    print(f"100mm is equal to {mm_to_inches(100):.4f} inches")
conversion_factor = {
    'mm_to_inches': 0.0393701
}

def mm_to_inches(mm):
    return mm * conversion_factor['mm_to_inches']

if __name__ == '__main__':
    print(f"25 mm is equal to {mm_to_inches(25):.4f} inches")
    print(f"100 mm is equal to {mm_to_inches(100):.4f} inches")
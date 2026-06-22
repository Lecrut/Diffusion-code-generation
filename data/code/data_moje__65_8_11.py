def feet_to_inches(feet):
    return feet * 12

def main():
    feet = 12
    inches = feet_to_inches(feet)
    assert inches == 144, f"Expected 144 inches, got {inches}"
    print(inches)

if __name__ == '__main__':
    main()
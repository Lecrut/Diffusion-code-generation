import sys
def validate_choice(choice):
    if choice not in ['A', 'B']:
        return False
    return True
def main():
    primary_input = "C"
    if not validate_choice(primary_input):
        fallback_input = "B"
        print(f"Fallback activated using: {fallback_input}")
    else:
        print(f"Primary input accepted: {primary_input}")
if __name__ == '__main__':
    main()
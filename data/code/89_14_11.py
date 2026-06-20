class BooleanOperations:
    def and_operation(self, state1: bool, state2: bool) -> bool:
        return state1 and state2

def main():
    bo = BooleanOperations()
    result = bo.and_operation(True, False)
    print(f"Result of AND operation on True and False is: {result}")

if __name__ == '__main__':
    main()
def check_contradiction(statement1: str, statement2: str) -> bool:
    return not (statement1 == statement2)

if __name__ == '__main__':
    print(check_contradiction("2+2=4", "2+2=5"))
    print(check_contradiction("3*3=9", "3*3=9"))
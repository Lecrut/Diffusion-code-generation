CONDITIONS = [
    lambda: True,
    lambda: False,
    lambda: True
]

class ConditionChecker:
    def check_all(self):
        return all(condition() for condition in CONDITIONS)

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check_all()
    print(f"All conditions met: {result}")
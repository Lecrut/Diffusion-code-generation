from typing import List

class PresenceChecker:
    @staticmethod
    def check_presence(target_list: List[int], master_list: List[int]) -> bool:
        return any(item in set(master_list) for item in target_list)

if __name__ == '__main__':
    checker = PresenceChecker()
    target = [1, 5, 9, 12]
    master = list(range(1, 100))
    result = checker.check_presence(target, master)
    print(result)
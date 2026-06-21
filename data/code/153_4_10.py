from typing import List

class PresenceChecker:
    def __init__(self, master_list: List[int]):
        self.master_set = set(master_list)

    def check_presence(self, target_list: List[int]) -> bool:
        for item in target_list:
            if item in self.master_set:
                return True
        return False

if __name__ == '__main__':
    checker = PresenceChecker(list(range(1, 100)))
    print(checker.check_presence([1, 5, 9, 12]))
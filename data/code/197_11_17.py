class ElementChecker:

    def __init__(self):
        self.target_set = set()

    def add_to_target(self, element):
        self.target_set.add(element)

    def check_elements(self, query_list):
        return not query_list.isdisjoint(self.target_set)
if __name__ == '__main__':
    checker = ElementChecker()
    checker.add_to_target('apple')
    checker.add_to_target('banana')
    print(checker.check_elements({'orange', 'banana'}))
    print(checker.check_elements({'grapefruit', 'kiwi'}))
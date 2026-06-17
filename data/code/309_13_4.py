class SetSummer:
    def sum_elements(self, data):
        total = 0
        for item in data:
            if isinstance(item, (int, float)):
                total += item
        return total
if __name__ == '__main__':
    summer = SetSummer()
    sample_list = [1, 5, 'a', 10.5, 3, 'b']
    result = summer.sum_elements(sample_list)
    print(result)
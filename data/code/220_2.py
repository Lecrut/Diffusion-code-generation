class SetAverager:
    def get_overall_average(self, list_of_sets):
        total_sum = 0
        total_count = 0
        for s in list_of_sets:
            for element in s:
                total_sum += element
                total_count += 1
        if total_count == 0:
            return 0
        return total_sum / total_count
if __name__ == '__main__':
    averager = SetAverager()
    set1 = {1, 2, 3}
    set2 = {4, 5}
    set3 = {6, 7, 8}
    set4 = {}
    list_of_sets = [set1, set2, set3, set4]
    average = averager.get_overall_average(list_of_sets)
    print(average)
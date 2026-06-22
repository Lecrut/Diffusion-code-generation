class ListAnalyzer:
    def get_middle_value(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        total_items = len(data)
        center_position = total_items // 2
        if total_items % 2 != 0:
            return data[center_position]
        left_center = data[center_position - 1]
        right_center = data[center_position]
        return (left_center + right_center) / 2

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    odd_sample = [100, 200, 300, 400, 500, 600, 700]
    even_sample = [10, 20, 30, 40]
    odd_result = analyzer.get_middle_value(odd_sample)
    even_result = analyzer.get_middle_value(even_sample)
    print(odd_result)
    print(even_result)
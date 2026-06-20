class EdgeElementFetcher:
    @staticmethod
    def get_edge_elements(lst):
        if not lst:
            return None, None
        return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first, last = EdgeElementFetcher.get_edge_elements(sample_list)
    print(f"First element: {first}")
    print(f"Last element: {last}")
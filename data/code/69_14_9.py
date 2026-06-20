class ListElementFetcher:
    def fetch_elements(self, lst):
        if not lst:
            return ()
        
        first_element = lst[0]
        last_element = lst[-1]
        middle_index = len(lst) // 2
        middle_element = lst[middle_index]
        
        return (first_element, last_element, middle_element)

if __name__ == '__main__':
    fetcher = ListElementFetcher()
    sample_list = [10, 20, 30, 40, 50]
    result = fetcher.fetch_elements(sample_list)
    print(result)
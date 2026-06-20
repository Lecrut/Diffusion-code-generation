class TimestampSorter:
    @staticmethod
    def sort_timestamps(timestamp_list):
        return sorted(timestamp_list)

if __name__ == '__main__':
    sample_timestamps = [1633024800, 1633111200, 1632938400]
    sorter = TimestampSorter()
    sorted_timestamps = sorter.sort_timestamps(sample_timestamps)
    print(sorted_timestamps)
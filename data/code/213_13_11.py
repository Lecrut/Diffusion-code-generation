class KthSmallestElement:
    @staticmethod
    def find_kth_smallest(nums, k):
        if not nums or k <= 0:
            return None

        pivot = nums[0]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if len(left) >= k:
            return KthSmallestElement.find_kth_smallest(left, k)
        elif len(left) + len(middle) >= k:
            return middle[0]
        else:
            return KthSmallestElement.find_kth_smallest(right, k - len(left) - len(middle))

if __name__ == '__main__':
    sample_data = [10, 20, 35, 42, 50]
    k = 3
    result = KthSmallestElement.find_kth_smallest(sample_data, k)
    print(f"The {k}-th smallest element is: {result}")
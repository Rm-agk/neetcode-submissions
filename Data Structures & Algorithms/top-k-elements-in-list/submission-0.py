from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        most_common = count.most_common(k)

        result = []

        for num, freq in most_common:
            result.append(num)

        return result
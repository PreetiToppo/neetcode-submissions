class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap to store frequency of each number
        count = {}
        for num in nums:
            count[num] = 1+count.get(num,0)

        # Build a list of [frequency,number] pairs from the map
        arr = []

        for num,cnt in count.items():
            arr.append([cnt,num])
        #Sort this list in ascending order based on frequency
        arr.sort()

        #Create an empty list for result
        res = []
        #Repeatedly pop from end of the sorted list and append the number in result
        while len(res)<k:
            res.append(arr.pop()[1])

        #Return result
        return res
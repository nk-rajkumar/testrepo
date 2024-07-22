class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            middle=(low+high)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                high=middle-1
            else:
                low=middle+1
        return high+1

a=Solution()
nums=[1]
target=8
b=a.searchInsert(nums,target)
print(b)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l<=r:
            mid = l + (r - l) // 2
            
            if nums[mid]==target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
                
        return l

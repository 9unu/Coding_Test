"""
https://leetcode.com/problems/two-sum/
1. Two Sum
정수가 저장된 배열 nums
nums의 원소 중 두 숫자를 더해서 target값이 될 수 있으면 true, 아니면 false 반환
같은 원소를 두번 사용 x

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

=> 10^4안에 끝내야함 -> n^2이내의 알고리즘으로 풀어야함 (되도록이면 nlogn)
"""

"""
접근 방법

1. 직관적으로 생각
- 보통 완전 탐색
- 단순화해서 생각
- 극한화해서 생각

2. 자료구조와 알고리즘 활용
- 문제이해를 바탕으로 어떤 자료구조를 사용하는게 적합한지 결정
- 대놓고 특정 자료구조, 알고리즘을 묻는 문제도 있음
- 자료구조에 따라 선택할 수 있는 알고리즘을 문제에 적용
"""

def twoSum(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j]==target):
                return True    
    return False

print(twoSum(nums = [3,2,4], target = 6))


# 시간 복잡도 낮추기

# 일단 오름차순 정렬 (nlogn)
# 맨왼쪽, 맨 오른쪽에 포인터
# 두개를 더해서 타겟보다 크면 오른쪽을 왼쪽으로 이동
# 작으면 왼쪽 포인터를 오른쪽으로 이동
# 두 포인터가 만나면 False
# 가능한 이유 : 두개를 더해서 target 값보다 작으면 왼쪽거를 더 왼쪽으로 보내도 어차피  더 작아짐, 반대도 똑같음
# 심지어 줄이다가 target값보다 작아지면, 오른쪽거를 다시 오른쪽거로 옮기면 됨
class Solution(object):
    def twoSum(self, nums, target):
        origin_nums=list(nums)
        nums.sort()
        l,r=0, len(nums)-1
        while(l<r):
            if(nums[l]+nums[r]<target):
                l+=1
            elif (nums[l]+nums[r]>target):
                r-=1
            elif (nums[l]+nums[r]==target):
                    break
            else:
                return False
        
        for i in range(len(origin_nums)):
            if(origin_nums[i]==nums[l]):
                a=i
        for j in range(len(origin_nums)-1,-1,-1):
            print(j)
            if(origin_nums[j]==nums[r]):
                b=j
        return [a,b]

        
def min_lateness(nums):
    nums.sort(key = lambda x : x[-1])
    
    lateness = 0
    processing = 0
    for unit,time in nums:
        processing += unit
        if processing > time:
            lateness += (processing - time)
    
    return lateness

k = min_lateness([[3,6],[1,9],[3,14],[2,8],[4,9],[2,15]])
print(k)

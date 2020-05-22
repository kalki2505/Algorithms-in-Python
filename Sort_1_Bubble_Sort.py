def bubble_sort(nums):
    def swap(a, b):
        temp = a
        a = b
        b = temp
        return a,b

    swapped = False
    pass_count = 0
    while not swapped:
        pass_count += 1
        print("\n\t\t\t>>>> Pass ", pass_count)
        swaps = 0
        print('Initial List: ', nums, '\tTotal swaps = ', swaps)
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = swap(nums[i], nums[i+1])
                swaps += 1
            print('\t\tList: ', nums, '\tTotal swaps = ', swaps)
        if swaps == 0:
            swapped = True
        print('Swapped = ', swapped, 'and total swaps = ', swaps, end = "\n\n")
    return nums


nums = [5, 4, 3, 2, 1]
print('Initial list: ', nums)
print('Final Sorted list: ', bubble_sort(nums))

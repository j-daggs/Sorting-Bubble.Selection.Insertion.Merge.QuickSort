#  John Daggs

#  11/18/2021f

#  Purpose of Lab07.py:
#  The purpose of Lab07.py is to define 5 different sorting functions, each utilizing a different sorting method:
#  Bubble, Selection, Insertion, Merge, and QuickSort.
#  Then, each sorting function is utilized in main for testing.
#

#  collaborators/resources -
#  Class Notes/Powerpoint/Code Examples/Textbook on Sorting

def bubble_sort(a_list):
    '''
    Bubble Sort:
    1) Is this sort stable or not stable?
        - stable
    2) Is this sort in-place or does it use extra memory?
        - in-place
    3) What is the running time of this sort? What are the expensive operations in the algorithm? Worst case?
        - Running Time: O(n^2)
        - Expensive Operations: Exchange operations . . . must exchange items before it knows final location of an item
        - Worst Case: When the list is in the reverse order, O(n^2)
    4) When would this sort be used? or not?
        - can be used to most efficiently tell whether list is already sorted . . . generally not efficient
        - most easily used with linked lists or array-based lists
    '''
    for i in range(len(a_list) - 1, 0, -1):  # looping through list with iterative value i (index); starting at the
        #  index equal to the length of the list minus 1, stopping at index zero, decrementing by 1 at the end of each
        #  loop
        for j in range(i):  # nested for loop, looping through with iterative value j in the range of i
            if a_list[j] > a_list[j + 1]:  # if the item at index j in the list is greater than the item at the index
                # one above j.
                temp = a_list[j]  # temporary variable set to the value at index j in the list
                a_list[j] = a_list[j + 1]  # setting index j in the list to the value at the index above it
                a_list[j + 1] = temp  # setting the index one above j in the list to the temporary variable
                # lines 22 and 23 swap the values . . .


def selection_sort(a_list):
    '''
    Selection Sort:
    1) Is this sort stable or not stable?
        - not stable
    2) Is this sort in-place or does it use extra memory?
        - in-place
    3) What is the running time of this sort? What are the expensive operations in the algorithm? Worst case?
        - Running Time: O(n^2)
        - Expensive Operations: Comparisons
        - Worst Case: When the list is in reverse order, O(n^2)
    4) When would this sort be used? or not?
        - if list is already sorted, if memory space is limited . . . does not work well with large datasets
    '''
    for i, item in enumerate(a_list):  # looping through i time based on amount of item in list by enumerating through
        # the list
        min_index = len(a_list) - 1  # setting the min index value to the length of the list minus one
        for j in range(i, len(a_list)):  # looping through for iterative value j, starting at value i, stopping at the
            # value of the length of the list
            if a_list[j] < a_list[min_index]:  # if the value at the index j of the list is less than the
                min_index = j  # the min index value is set to the value j
        if min_index != i:  # if the min index value is not equal to the value i
            a_list[min_index], a_list[i] = a_list[i], a_list[min_index]  # swapping value at index min index in the list
            # with the value at index i in the list


def insertion_sort(a_list):
    '''
    Insertion Sort:
    1) Is this sort stable or not stable?
        - Stable
    2) Is this sort in-place or does it use extra memory?
        - in-place
    3) What is the running time of this sort? What are the expensive operations in the algorithm? Worst case?
        - Running Time: O(n^2)
        - Expensive Operations: Comparisons
        - Worst Case: When the list is in reverse order, O(n^2)
    4) When would this sort be used? or not?
        - for smaller array, when only a small amount of elements are out of place . . . does not work well with large
        datasets . . .
    '''
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val


def merge_sort(a_list):
    '''
    Merge Sort:
    1) Is this sort stable or not stable?
        - Stable
    2) Is this sort in-place or does it use extra memory?
        - uses extra memory
    3) What is the running time of this sort? What are the expensive operations in the algorithm? Worst case?
        - Running Time: O(n*logn)
        - Expensive Operations: Splitting, Merging
        - Worst Case: maintains O(n*logn) regardless of the list and its order when passed to function
    4) When would this sort be used? or not?
        -Useful in sorting linked lists . . . slower for small arrays, random array based data
    '''
    if len(a_list) > 1:  # loops, if the length of the list is greater than one
        mid = len(a_list) // 2  # mid initialized to the length of the list DIV 2
        left_half = a_list[:mid]  # initializing the left half of the list to a variable left half
        right_half = a_list[mid:] # initializing the right half of the list to a variable right half

        merge_sort(left_half)  # recursive merge sort call on left half
        merge_sort(right_half)  # recursive merge sort call on right half

        i = 0  # initialize i
        j = 0  # initialize j
        k = 0  # initialize k
        while i < len(left_half) and j < len(right_half):  # loops while i is less than the length of the left half list
            # and j is less than the length of the right half list
            if left_half[i] <= right_half[j]:  # if the value of the left half at index i is less than or equal to the
                # value at index j in the right half
                a_list[k] = left_half[i]  # the value of the list at index k is set to the value of the left half at
                # index i
                i = i + 1  # incrementing i by one
            else:  # else ...
                a_list[k] = right_half[j]  # the value of the list at index k is set to the value of the right half at
                # index i
                j = j + 1  # incrementing j by one
            k = k + 1  # incrementing k by one

        while i < len(left_half):  # loops while i is less than the length of the left half
            a_list[k] = left_half[i]  # the value of the list at index k is set to the value of the left half at
            # index i
            i = i + 1  # incrementing i by one
            k = k + 1  # incrementing k by one

        while j < len(right_half): # loops while j is less than the length of the left half
            a_list[k] = right_half[j]
            j = j + 1  # incrementing j by one
            k = k + 1  # incrementing k by one


def quick_sort(a_list):
    '''
    Quick Sort:
    1) Is this sort stable or not stable?
        - Stable
    2) Is this sort in-place or does it use extra memory?
        - in-place
    3) What is the running time of this sort? What are the expensive operations in the algorithm? Worst case?
        - Running Time: O(n*logn)
        - Expensive Operations: Finding the split point
        - Worst Case: When called on a list that is already sorted
    4) When would this sort be used? or not?
        -For shorter list . . . larger lists do not run well with quick sort
    '''
    quick_sort_helper(a_list, 0, len(a_list) - 1)  # calling the quick sort helper function; passing the list, zero as
    # the parameter first, and the length of the list minus one to the parameter last


def quick_sort_helper(a_list, first, last):
    if first < last:  # if the value passed to parameter first is less than the value passed to parameter last
        split = partition(a_list, first, last)  # split value set to the return value of calling the partition function;
        # passing the list to the list parameter, first to the parameter first, and last to the parameter last
        quick_sort_helper(a_list, first, split - 1)  # recursive call of quick sort helper function; passing the list
        # to the list parameter, first to the first parameter, and split minus one to the parameter last
        quick_sort_helper(a_list, split + 1, last)  # recursive call of quick sort helper function; passing the list
        # to the list parameter, split minus one to the parameter first, and last to the parameter last


def partition(a_list, first, last):
    pivot_val = a_list[first]  # initializing the partition pivot value
    left_mark = first + 1  # initializing left_mark to the value passed to the first parameter plus one
    right_mark = last  # initializing right_mark to the value passed to the last parameter
    done = False  # initializing done to False

    while not done:  # loops while done = false
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:  # loops, while the left mark is less than or
            # equal to the right mark and while the value at the index left_mark in the list is less than or equal to
            # the pivot value
            left_mark = left_mark + 1  # incrementing left mark value by one
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:  # loops, while the left mark is less than or
            # equal to the right mark and while the value at the index right_mark in the list is less than or equal to
            # the pivot value
            right_mark = right_mark - 1  # decrementing the right mark value by one
        if right_mark < left_mark:  # if the right mark is less than the left mark,
            done = True  # then done is set to True
        else:  # else . . .
            a_list[left_mark], a_list[right_mark] = (a_list[right_mark], a_list[left_mark],)  # swapping left mark and
            # right mark in the list
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]  # swapping value at index first in the list
    # with the value at index right mark in the list

    return right_mark  # returning right mark


def main():

    # bubble sort . . .
    print(bubble_sort.__doc__)
    a_list = [2, 9, 100, 25, 1, 37, 14, 86, 0, 77, 93, 0.0, 600, 900, 21]
    print("list before bubble sort: ", str(a_list))
    bubble_sort(a_list)
    print("list after bubble sort: ", a_list)
    print("**********************************************************************************************************")
    # selection sort . . .
    print(selection_sort.__doc__)
    a_list = [5, 236, 13, 79, 40, 1, 51, 22, 13.0, 900, 901, 101]
    print("\nlist before selection sort: ", str(a_list))
    selection_sort(a_list)
    print("list after selection sort: ", a_list)
    print("**********************************************************************************************************")
    # insertion sort . . .
    print(insertion_sort.__doc__)
    a_list = [100, 89, 1, 7, 30, 7.0, 50, 1000, 209, 6, 333]
    print("\nlist before insertion sort: ", str(a_list))
    insertion_sort(a_list)
    print("list after insertion sort: ", a_list)
    print("**********************************************************************************************************")
    # merge sort . . .
    print(merge_sort.__doc__)
    a_list = [44, 7, 970, 19, 1007, 1, 70, 62, 233, 6034, 9999, 1.0, 20403]
    print("\nlist before merge sort: ", str(a_list))
    merge_sort(a_list)
    print("list after merge sort: ", a_list)
    print("**********************************************************************************************************")
    # quick sort . . .
    print(quick_sort.__doc__)
    a_list = [15, 16, 2, 63, 3, 10000, 3.0, 82, 5, 82, 999]
    print("\nlist before quick sort: ", str(a_list))
    quick_sort(a_list)
    print("list after quick sort: ", a_list)

    quick_sort([2, 5, 1, 7, 9, 12, 11, 10])

main()
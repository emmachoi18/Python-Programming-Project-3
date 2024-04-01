"""
This module is a collection of statistical functions for analyzing
the results of a non-nominal survey question.

To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canavs for more information.

Author name: Emma Choi
I have neither given nor received unauthorized assistance on
this assignment. I did not fabricate the answers to my
survey question.
"""
__version__ = 1

# 0) Question and Results
SURVEY_QUESTION = "How many wishes would you ask for if you stumbled upon a magical genie lamp?"
SURVEY_RESULTS = [3, 3, 1000, 100, 500, 10000, 500, 4, 150, 5000]

# 1) count
def count(SURVEY_RESULTS):
    '''
    count function consumes a list of numbers and returns an integer
    representing the length of the list.

    Args:
        list: SURVEY_RESULTS
    Returns:
        int: count
    '''
    count = 0
    for result in SURVEY_RESULTS:
        count += 1
    return count

# 2) summate
def summate(SURVEY_RESULTS):
    '''
    summate function consumes a list of numbers and returns an integer
    representing the total sum of all the numbers in the list.

    Args:
        list: SURVEY_RESULTS
    Returns:
        int: summate
    '''
    summate = 0
    for result in SURVEY_RESULTS:
        summate += result
    return summate

# 3) mean
def mean(SURVEY_RESULTS):
    '''
    mean function consumes a list of numbers and returns a float value that
    represents the mean of the list. The formula used is mean = sum / count.
    If the list is empty, None is returned. Otherwise, the mean is rounded
    to two decimal places using the built-in round function and returned.

    Args:
        list: SURVEY_RESULTS
    Returns:
        None or float
    '''
    if count(SURVEY_RESULTS) == 0:
        return None
    else:
        countOfNums = count(SURVEY_RESULTS)
        sumOfNums = summate(SURVEY_RESULTS)
        return round(sumOfNums / countOfNums, 2)

# 4) maximum
def maximum(SURVEY_RESULTS):
    '''
    maximum function consumes a list of numbers and returns the highest number
    from the list. If the list is empty, None is returned.
    
    Args:
        list: SURVEY_RESULTS
    Returns:
        None or int: maximum
    '''
    if count(SURVEY_RESULTS) == 0:
        return None
    else:
        maximum = SURVEY_RESULTS[0]
        for result in SURVEY_RESULTS:
            if result > maximum:
                maximum = result
        return maximum

# 5) minimum
def minimum(SURVEY_RESULTS):
    '''
    minimum function consumes a list of numbers and returns the lowest number
    from the list. If the list is empty, None is returned.

    Args:
        list: SURVEY_RESULTS
    Returns:
        None or int: minimum
    '''
    if count(SURVEY_RESULTS) == 0:
        return None
    else:
        minimum = SURVEY_RESULTS[0]
        for result in SURVEY_RESULTS:
            if result < minimum:
                minimum = result
        return minimum

# 6) median
def median(SURVEY_RESULTS):
    '''
    median function consumes a list of numbers and returns the median number
    from the list. If the list is empty, None is returned. The list is first
    sorted using the built-in sorted function. Then, middle index = length / 2
    is used to calculate the median. The average in the even case is not
    taken into consideration in this median function.

    Args:
        list: SURVEY_RESULTS
    Returns:
        int
    '''
    if count(SURVEY_RESULTS) == 0:
        return None
    else:
        sortedResults = sorted(SURVEY_RESULTS)
        middleIndex = count(sortedResults) // 2
        return sortedResults[middleIndex]
        
# 7) square
def square(SURVEY_RESULTS):
    '''
    square function consumes a list of numbers and returns a new list of nums
    where each element has been squared.

    Args:
        list: SURVEY_RESULTS
    Returns:
        list
    '''
    return [num ** 2 for num in SURVEY_RESULTS]

# 8) standard_deviation
def standard_deviation(SURVEY_RESULTS):
    '''
    standard_deviation function consumes a list of numbers and returns a float
    representing their standard deviation. If the list has fewer than two
    elements, None is returned. The standard deviation is rounded to two decimal
    places and then returned.

    Args:
        list: SURVEY_RESULTS
    Returns:
        float
    '''
    if count(SURVEY_RESULTS) < 2:
        return None
    else:
        sumOfValuesSquared = summate(square(SURVEY_RESULTS))
        sumOfValues = summate(SURVEY_RESULTS)
        countOfValues = count(SURVEY_RESULTS)
        stdev = (((sumOfValuesSquared) - (sumOfValues ** 2) / (countOfValues)) / (countOfValues - 1)) ** 0.5
        return round(stdev, 2)

# The following code can be used to try out your functions.
# Uncomment each line as you implement the functions to try them out.
# When you have implemented each function, copy the output from the
#   console into a comment below.
if __name__ == "__main__":
    print("We asked", count(SURVEY_RESULTS), "people the following question.")
    print('"'+SURVEY_QUESTION+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(SURVEY_RESULTS))
    print("\tMean:", mean(SURVEY_RESULTS))
    print("\tMedian:", median(SURVEY_RESULTS))
    print("\tMaximum:", maximum(SURVEY_RESULTS))
    print("\tMinimum:", minimum(SURVEY_RESULTS))
    print("\tStandard Deviation:", standard_deviation(SURVEY_RESULTS))
    
'''
Output:
    We asked 10 people the following question.
    "How many wishes would you ask for if you stumbled upon a magical genie lamp?"
    Here are the statistical results:
    	Sum: 17260
    	Mean: 1726.0
    	Median: 500
    	Maximum: 10000
    	Minimum: 3
    	Standard Deviation: 3278.58
'''
    
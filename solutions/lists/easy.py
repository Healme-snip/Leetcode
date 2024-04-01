""" Easy List Problems """


class ListNode:
    """ Definition for singly-linked list """
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class SolutionMergeTwoLists(object):
    """ 21. Merge Two Sorted Lists """
    def merge_two_lists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        r = result

        while list1 and list2:
            if list1.val >= list2.val:
                r.next = list2
                list2 = list2.next
            else:
                r.next = list1
                list1 = list1.next
            r = r.next

        if list1 is not None:
            r.next = list1
        elif list2 is not None:
            r.next = list2

        return result.next

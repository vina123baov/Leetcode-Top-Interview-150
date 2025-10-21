class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # Con trỏ cho phần dữ liệu thực của nums1
        j = n - 1  # Con trỏ cho nums2
        k = m + n - 1  # Con trỏ cho vị trí cuối nums1
        
        # Hợp nhất từ cuối về đầu
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Nếu nums2 còn thừa, copy vào nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
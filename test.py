# 第一个脚本
import cv2
# 读取
img_path = "../image/test01.png"
out_path = "../out/output.png"
img = cv2.imread(img_path)
if img is None:
    print("读取失败：图片路径不对，或者文件不存在")
else:
    # 打印图片
    print("图片尺寸：",img.shape)
# 在窗口显示
    cv2.imshow("test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(out_path,img)
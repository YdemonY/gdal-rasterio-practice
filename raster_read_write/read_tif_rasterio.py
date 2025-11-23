import rasterio

tif_path = "example.tif"  # 先占位，未来换成真实路径

with rasterio.open(tif_path) as src:
    print("宽 x 高:", src.width, src.height)
    print("波段数:", src.count)
    print("坐标参考系:", src.crs)
    print("仿射变换:", src.transform)

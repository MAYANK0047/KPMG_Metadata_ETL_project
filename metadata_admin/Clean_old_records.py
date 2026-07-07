# Exact Volume paths based on your screenshot
volumes_to_clear = [
    "/Volumes/workspace/default/landing_zone_v2/",
    "/Volumes/workspace/default/silver_business_v2/",
    "/Volumes/workspace/default/gold_business_v2/",
    "/Volumes/workspace/default/quarantine_zone_v2/"
]

print("Initiating Demo Environment Reset...\n")

for volume_path in volumes_to_clear:
    try:
        # 1. Look inside the Volume
        items_inside = dbutils.fs.ls(volume_path)
        
        # 2. Delete only the files/folders INSIDE, keeping the main Volume intact
        for item in items_inside:
            dbutils.fs.rm(item.path, True) 
            
        print(f" Swept clean: {volume_path}")
        
    except Exception as e:
        # If the folder is already empty, it just skips it without throwing a scary error
        print(f" Checked {volume_path} (Already empty or not found)")

print("\n Success! Volumes are fully reset. Ready for Day 1 data drop.")
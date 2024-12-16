import polib
from googletrans import Translator
# Load the .po file
po_file = polib.pofile('test_po.po')

# Print metadata
print("Metadata:")
print(po_file.metadata)

# Iterate through entries
print("\nTranslations:")
counter=0
count_of_entrys=len(po_file)
for entry in po_file:
    print(f"Original: {entry.msgid}")
    print(f"Translated: {entry.msgstr}")
    counter+=1
    print(f"{counter}/{count_of_entrys}")
    if entry.msgstr=="":
        try:
            translator = Translator()
            result = translator.translate(entry.msgid, src='en', dest='fa')
            entry.msgstr=result.text
            po_file.save()
        except:
            continue
        
        



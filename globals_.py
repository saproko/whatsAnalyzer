DATEPATTERN_IOS = r"^\[\d\d\.\d\d\.\d\d,\s\d\d:\d\d:\d\d\]"
DATEPATTERN_ANDROID = r"\d\d\.\d\d\.\d\d,\s\d\d:\d\d"

DATEPARSE_IOS = "[%d.%m.%y, %H:%M:%S]"
DATEPARSE_ANDROID = "%d.%m.%y, %H:%M"

PREFIX_PATTERN_IOS = fr"{DATEPATTERN_IOS}\s.+?:\s"
PREFIX_PATTERN_ANDROID = fr"{DATEPATTERN_ANDROID}\s-\s.+?:\s"

CAPTURE_NAME_PATTERN_IOS = fr"{DATEPATTERN_IOS}\s(.+?):"
CAPTURE_NAME_PATTERN_ANDROID = fr"{DATEPATTERN_ANDROID}\s-\s(.+?):\s"

CAPTURE_MEDIA_PATTERN_IOS = fr"{PREFIX_PATTERN_IOS}(\w+)\sweggelassen$"
CAPTURE_MEDIA_PATTERN_ANDROID = fr"{PREFIX_PATTERN_ANDROID}<(Medien) ausgeschlossen>$"

# https://github.com/PetengDedet/WhatsApp-Analyzer/blob/master/stop-words/german.txt
STOPWORDS = ["aber", "alle", "allem", "allen", "aller", "alles", "als", "also", "am", "an", "ander", "andere", "anderem", "anderen", "anderer", "anderes", "anderm", "andern", "anders", "auch", "auf", "aus", "bei", "bin", "bis", "bist", "da", "damit", "dann", "das", "dass", "dasselbe", "dazu", "daß", "dein", "deine", "deinem", "deinen", "deiner", "deines", "dem", "demselben", "den", "denn", "denselben", "der", "derer", "derselbe", "derselben", "des", "desselben", "dessen", "dich", "die", "dies", "diese", "dieselbe", "dieselben", "diesem", "diesen", "dieser", "dieses", "dir", "doch", "dort", "du", "durch", "ein", "eine", "einem", "einen", "einer", "eines", "einig", "einige", "einigem", "einigen", "einiger", "einiges", "einmal", "er", "es", "etwas", "euch", "euer", "eure", "eurem", "euren", "eurer", "eures", "für", "gegen", "gewesen", "hab", "habe", "haben", "hat", "hatte", "hatten", "hier", "hin", "hinter", "ich", "ihm", "ihn", "ihnen", "ihr", "ihre", "ihrem", "ihren", "ihrer", "ihres", "im", "in", "indem", "ins", "ist", "jede", "jedem", "jeden", "jeder", "jedes", "jene", "jenem", "jenen", "jener", "jenes", "jetzt", "kann", "kein", "keine", "keinem", "keinen", "keiner", "keines", "können", "könnte", "machen",
             "man", "manche", "manchem", "manchen", "mancher", "manches", "mein", "meine", "meinem", "meinen", "meiner", "meines", "mich", "mir", "mit", "muss", "musste", "nach", "nicht", "nichts", "noch", "nun", "nur", "ob", "oder", "ohne", "sehr", "sein", "seine", "seinem", "seinen", "seiner", "seines", "selbst", "sich", "sie", "sind", "so", "solche", "solchem", "solchen", "solcher", "solches", "soll", "sollte", "sondern", "sonst", "um", "und", "uns", "unser", "unsere", "unserem", "unseren", "unserer", "unseres", "unter", "viel", "vom", "von", "vor", "war", "waren", "warst", "was", "weg", "weil", "weiter", "welche", "welchem", "welchen", "welcher", "welches", "wenn", "werde", "werden", "wie", "wieder", "will", "wir", "wird", "wirst", "wo", "wollen", "wollte", "während", "würde", "würden", "zu", "zum", "zur", "zwar", "zwischen", "über", "ja", "nein", "mal", "ne", "jo", "einfach", "immer", "gut", "s", "für", "hast", "mehr", "sagen", "glaube", "geht", "ok", "morgen", "halt", "gerade", "eigentlich", "schon", "wer", "gar", "macht", "gemacht", "i", "richtig", "bekommen", "irgendwie", "wäre", "ab", "heute", "viele", "habt", "genau", "gibt", "wei", "je", "mache", "c", "kommt", "finde", "h", "jemand", "gesagt", "warum"]

from aqt import mw, gui_hooks

def config() -> dict[str, str]:
    return mw.addonManager.getConfig(__name__)

def multipaste(editor) -> None:
    text = editor.mw.app.clipboard().text()
    sep = config().get('separator', '\t')
    splits = text.split(sep)
    for i, s in enumerate(splits):
        idx = editor.currentField + i
        if idx >= len(editor.note.fields):
            break
        editor.note.fields[editor.currentField + i] = s
    editor.loadNoteKeepingFocus()

def setup_shortcuts(shortcuts, editor) -> None:
    hotkey_multipaste = config().get('multipaste_key', 'Ctrl+m')
    shortcuts.append((hotkey_multipaste, lambda: multipaste(editor)))

gui_hooks.editor_did_init_shortcuts.append(setup_shortcuts)

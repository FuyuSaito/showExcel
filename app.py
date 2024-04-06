import streamlit as st
import pandas as pd

def main():
    st.title("Excel Viewer")

    # エクセルファイルのアップロード
    uploaded_file = st.file_uploader("エクセルファイルをアップロードしてください", type=["xlsx"])

    if uploaded_file is not None:
        try:
            # エクセルファイルを読み込む
            xls = pd.ExcelFile(uploaded_file)
            sheet_names = xls.sheet_names

            # シート名の一覧を表示
            st.write("シート一覧:")
            selected_sheet_name = st.selectbox("表示するシートを選択してください", sheet_names)

            # 指定されたシートのデータを読み込む
            df = pd.read_excel(uploaded_file, sheet_name=selected_sheet_name)

            # デフォルトで全ての行を表示
            max_rows = len(df)

            # 表示する行数を指定
            row_count = st.number_input("表示する行数を入力してください", min_value=1, max_value=len(df), value=len(df))

            # 表示するデータが多い場合は、展開可能なセクションを作成して表示
            st.table(df.head(row_count))


        except Exception as e:
            st.error("エラーが発生しました: {}".format(e))

if __name__ == "__main__":
    main()
